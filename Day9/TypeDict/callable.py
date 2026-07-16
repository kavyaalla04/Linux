'''
Case study: Food Delivery application
The app can run in 3 environments:
Developmet
Testing
Production
'''

#Define configuration classes
class DevConfig:
    database= "sqlite.db"
    debug= True

class TestConfig:
    database= "test.db"
    debug= True

class ProdConfig:
    database= "mysql://food_app"
    debug= False

#Step 2: Define a configuration factory(Callable)
def get_config(environment):
    if environment == "dev":
        return DevConfig()
    elif environment == "test":
        return TestConfig()
    else:
        return ProdConfig()
    
#Step3: Use the factory
env = "dev"
config = get_config(env)
print(config.database)
print(config.debug)