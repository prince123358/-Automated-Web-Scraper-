from db.models import get_engine
import pandas as pd




def export_to_csv(db_path='sqlite:///scraper.db', out='export.csv'):
engine = get_engine(db_path)
df = pd.read_sql_table('scraped_items', con=engine)
df.to_csv(out, index=False)
print('Exported', len(df), 'rows to', out)




if __name__ == '__main__':
export_to_csv()
