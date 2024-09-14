import os
from sqlalchemy import create_engine, text
DATABASE_URL="cockroachdb://coronavirus:HHLLTQSUBYJK8MKZYvWr5Q@twitterbot-7607.6xw.aws-ap-southeast-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full"
engine = create_engine("cockroachdb://coronavirus:HHLLTQSUBYJK8MKZYvWr5Q@twitterbot-7607.6xw.aws-ap-southeast-1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full")
conn = engine.connect()

# res = conn.execute(text("SELECT now()")).fetchall()
# print(res)