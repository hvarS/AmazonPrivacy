import pandas as pd

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


links = pd.read_csv("scraping_2/com-2/get_profile_links/profile_links.csv")
links = list(links["Profile Links"])

evenLinks = chunks(links,1000)


