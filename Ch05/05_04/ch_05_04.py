import pandas as pd
df = pd.read_csv('taxi.csv.xz')
print(df.dtypes)
print(df.VendorID.sample(5))
vendor_names = {
    1 : 'Creative',
    2 : 'VeriFone',
    4: 'BigApple'
    }
vendors = df.VendorID.map(vendor_names)
print(vendors.sample(5))
cat_vendors = vendors.astype('category')
print(cat_vendors.sample(5))
print(cat_vendors.memory_usage(deep=True))
print(df.VendorID.memory_usage(deep=True))
print(vendors.memory_usage(deep=True))
