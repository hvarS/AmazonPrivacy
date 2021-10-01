import pandas as pd

filename = "./product_links.csv"

df = pd.read_csv(filename)

l = df.shape[0]
numpages = 50
modified_links = []

for i in range(l):
    link = df.iat[i, 0]
    index1 = link.find("dp/")
    index2 = link.find("?")
    id_prod = link[index1 + 3: index1 + 3 + 10]
    modified_base_link = "https://www.amazon.com/product-reviews/" + id_prod + "/ref_ref=cm_cr_arp_d_paging_btm_next_*?pageNumber=*"
    for i in range(numpages):
        modified_link = modified_base_link.replace('*', str(i+1))
        print(modified_link)
        modified_links.append(modified_link)

dict1 = {'Link': modified_links}
df1 = pd.DataFrame(dict1)
df1.to_csv('./review_links.csv', index=False)