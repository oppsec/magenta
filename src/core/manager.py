from random import randint

def get_user_agent(file_name: str = 'src/core/user-agents.txt') -> str:

    with open(file_name) as user_agents_file:
        user_agent = user_agents_file.readlines()
        user_agent = user_agent[randint(0, len(user_agent) -1)]
        user_agent = user_agent.encode('utf-8')

        return str(user_agent)


# Headers for requests
headers = {'User-Agent': get_user_agent()}

# Properties for requests
props = {
    'verify': False,
    'timeout': 10,
    'allow_redirects': True,
    'headers': headers
}