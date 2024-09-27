from console import HBNBCommand

# Create an instance of the command interpreter
cmd = HBNBCommand()

# Simulate input commands
cmd.onecmd('create State name="California"')
cmd.onecmd('create State name="Arizona"')
cmd.onecmd('all State')
cmd.onecmd('create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
cmd.onecmd('all Place')
