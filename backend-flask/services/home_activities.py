from datetime import datetime, timedelta, timezone
#Honeycomb
from opentelemetry import trace 
# pyscopg
from lib.db import pool, query_wrap_object, query_wrap_array

#Honeycomb
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    #logger.info("HomeActivities") #CloudWatch logs
    with tracer.start_as_current_span("home-activities-custom-span-mock-data"):  #Honeycomb custom span
      span = trace.get_current_span() #Honeycomb attribute
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat()) #Honeycomb attribute
      
      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      #span.set_attribute("app.result_length",len(results)) #Honeycomb 
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()   
      return json[0]
      return results