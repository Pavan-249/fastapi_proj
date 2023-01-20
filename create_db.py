from database import Base,engine
from models import baby


print('creating data...')

Base.metadata.create_all(engine)
