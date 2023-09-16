from requests import Session

class GitLabAPIRequestError(ValueError):
    pass

class GitLabAPIService(object):
    base_url: str = "https://gitlab.com/api/v4"
    request_session: Session = None
    timeout: int = 2

    def __init__(self, session: Session):
        self.request_session = session

    def get_all_users(self):
        url = self.base_url
        try:
            response = self.request_session.get(url, timeout=self.timeout)
        except Exception as x:
            print('It failed :(', x.__class__.__name__)
            raise GitLabAPIRequestError
        else:
            return response.json()['data']
