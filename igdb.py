import requests

class IGDB_Lib:

    def __init__(self) -> None:
        self.client_id = 'ewqwd3rsk9qj09ql7p2t80k5rhk8oi'
        self.client_secret = 'uygg57zqnuncv3ae06plv704rtmjh9'
        self.base_url = 'https://api.igdb.com/v4'

        self.token = self.get_access_token_from_twitch()



    def get_access_token_from_twitch(self) -> None:
        twitch_url = 'https://id.twitch.tv/oauth2/token'
        payload = { 
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }

        response = requests.post(url=twitch_url, data=payload)

        if response.status_code != 200:
            raise RuntimeError("Authentication Error:", response.status_code)
            return None
        
        data = response.json()
        return data.get('access_token')
        


    # Main wrapper function for all requests
    def igdb_request(self, endpoint, data) -> requests.Response:
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {self.token}',
        }
        response = requests.post(self.base_url + endpoint, headers=headers, data=data)

        # TODO: Look into throwing errors properly instead of printing error and return none
        if response.status_code != 200:
            raise RuntimeError("API Request Error:", response.status_code)

        
        return response.json()

    # Takes in a list of dictionaries and prints out the list of a specified field
    def print_results(self, objects_list, field_name):
        print([i.get(field_name) for i in objects_list])

    def get_company_name(self, company_names) -> str:
        return self.igdb_request(endpoint='/companies', data=f'fields name; where id = ({company_names});')









    def main(access_token) -> None:
        # 1: Search for specific game
        # 2: Return a list of companies associated with searched game

        # Declaring parameters
        game_name = 'persona'
        data = f'fields name, involved_companies; search "{game_name}"; limit 5; where parent_game = null & version_parent = null;'

        # Search results
        games = igdb_request(endpoint='/games', data=data, access_token=access_token)


        # Listing all companies associated with the search results
        companies = []
        for game in games:
            involved_companies = game['involved_companies']

            companies.extend(list(set(involved_companies) - set(companies)))




        # Print company names in a readable format
        print(', '.join(str(x) for x in companies))

        company_names = get_company_name(', '.join(str(x) for x in companies))

        print([company.get('name') for company in company_names])



    #Print a list of distinct companies returned by the search



    if __name__ == "__main__":
        access_token = get_access_token_from_twitch()

        main(access_token=access_token)  