import pandas as pd
import csv

df=pd.read_csv('final_data.csv')
print(df.shape)
del df['hyperlink']
del df['temp_mass']
del df['temp_date']
del df['pl_letter']
del df['pl_name']
del df['pl_controv_flag']
del df['pl_orbper']
del df['pl_orbpererr1']
del df['pl_orbpererr2']
del df['pl_orbperlim']
del df['pl_orbsmax']
del df['pl_orbsmaxerr1']
del df['pl_orbsmaxerr2']
del df['pl_orbsmaxlim']
del df['pl_orbeccen']
del df['pl_orbeccenerr1']
del df['pl_orbeccenerr2']
del df['pl_bmassj']
del df['pl_bmassjerr1']
del df['pl_bmassjerr2']
del df['pl_bmassjlim']
del df['pl_bmassprov']
del df['pl_radj']
del df['pl_radjerr1']
del df['pl_radjerr2']
del df['pl_orbtpererr1']
del df['pl_orbtpererr2']
del df['pl_orblper']
del df['pl_orblpererr1']
del df['pl_orblpererr2']
del df['pl_orblperlim']
del df['pl_rvamp']
del df['pl_rvamperr1']
del df['pl_rvamperr2']
del df['pl_rvamplim']
del df['pl_projobliq']
del df['pl_projobliqerr1']
del df['pl_projobliqerr2']
del df['pl_projobliqlim']
del df['pl_trueobliq']
del df['pl_trueobliqerr1']
del df['pl_trueobliqerr2']
del df['pl_trueobliqlim']

print(df.shape)
print(list(df))
df=df.rename({
    'hostname':'solar_system_name',
    'discoverymethod':'planet_discovery_method'
},axis='columns')
print(list(df))
df.to_csv('final3.csv')