# these are "boolean literals"
is_raining = False
is_cold = False

rain_input = input('Is it raining?')
temp_input = input('What is the temperature outside?')

user_yes = rain_input == 'yes'
print(user_yes)

if user_yes or rain_input == 'y':
    # is_raining is now no longer a literal!
    is_raining = True

if int(temp_input) < 60:
    is_cold = True


if is_cold and is_raining:
    print(':( :( :( :(')
elif is_cold or is_raining:
    print(':| :| :| :| :|')
else:
    print(':) :) :) :) :)')


def true_or_false():
    return is_raining


# this is now a boolean too!
outcome = true_or_false()
print(outcome)
