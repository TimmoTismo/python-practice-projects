import requests
from json import dumps

CLIENT_ID = 'ewqwd3rsk9qj09ql7p2t80k5rhk8oi'
CLIENT_SECRET = 'uygg57zqnuncv3ae06plv704rtmjh9'

BASE_URL = 'https://api.igdb.com/v4'


def get_access_token_from_twitch() -> str:
    twitch_url = 'https://id.twitch.tv/oauth2/token'
    payload = { 
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'client_credentials'
    }

    response = requests.post(url=twitch_url, data=payload)

    if response.status_code != 200:
        print("Access Token Error:", response.status_code)
        return None
    

    data = response.json()
    token = data.get('access_token')
    return token 
    

# Main wrapper function for all requests
def igdb_request(endpoint, data, access_token) -> requests.Response:
    headers = {
        'Client-ID': CLIENT_ID,
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.post(BASE_URL+endpoint, headers=headers, data=data)

    # TODO: Look into throwing errors properly instead of printing error and return none
    if response.status_code != 200:
        print("API Request Error:", response.status_code)
        return None
    
    return response.json()


def get_company_name(company_names) -> str:
    return igdb_request(endpoint='/companies', data=f'fields name; where id = ({company_names});')



def main(access_token) -> None:
    game_name = 'persona'
    data = f'fields name, involved_companies; search "{game_name}"; limit 5; where parent_game = null & version_parent = null;'

    games = igdb_request(endpoint='/games', data=data, access_token=access_token)


    companies = []
    for game in games:
        involved_companies = game['involved_companies']

        companies.extend(list(set(involved_companies) - set(companies)))

    print(', '.join(str(x) for x in companies))


    company_names = get_company_name(', '.join(str(x) for x in companies))

    print([company.get('name') for company in company_names])



#Print a list of distinct companies returned by the search



if __name__ == "__main__":
    access_token = get_access_token_from_twitch()

    main(access_token=access_token)  