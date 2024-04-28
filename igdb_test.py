from igdb import IGDB_Lib


def main():
    # 1: Search for specific game
    # 2: Return a list of companies associated with searched game

    # Initialise igdb object
    igdb_object = IGDB_Lib()


    # Declaring parameters
    game_name = 'tears of the kingdom'
    data = f'fields name, involved_companies; search "{game_name}"; limit 5; where parent_game = null & version_parent = null;'

    # Search results
    games = igdb_object.igdb_request(endpoint='/games', data=data)


    # Output search results
    print(games)



if __name__ == '__main__':
    main()