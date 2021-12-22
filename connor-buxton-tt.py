#!/usr/bin/env python
# coding: utf-8

# # Tournament Tracker
# ### By Connor Buxton
# Allows the user to create a tournament, add and remove participants, print out the list of participants as well as save their work to a CSV file.

# First, let's create the start where the user inputs the number of participants. If they don't input a number, discard their input and try asking them again.

# In[42]:


input_is_num = False

while not input_is_num:
    userNum = input('Enter the number of participants: ')

    if userNum.isdecimal():
        input_is_num = True
    else:
        print('That is not a number.')


# With the number of participants, we will initialize a dictionary with keys being numbers and values being participant names

# In[43]:


userNum = int(userNum)

participant_dict = {}

for i in range(1, userNum+1):
    participant_dict[i] = None


# Next step is to define a function for our main menu. Since we will have a loop ongoing until the user decides to quit, it would be a good idea to use functions.

# In[44]:


def main_menu():
    print('Welcome to TournamentTracker!')
    print('-----------------------------')
    print('1. Sign Up')
    print('2. Cancel Sign Up')
    print('3. View Participants')
    print('4. Save Changes')
    print('5. Exit')
    print()
    
    goodInput = False
    while not goodInput:
        userOption = input('What option would you like?: ')
        if userOption.isdecimal():
            userOption = int(userOption)
            if userOption > 0 and userOption < 6:
                return userOption
                goodInput = True
            else:
                print('That number falls outside our options. Please try again.')
                
        else:
            print('That input is not a number. Please try again.')


# Now that we have our main menu, let's make the participant sign up function:

# In[45]:


def part_sign_up(userNum):
    
    if None not in participant_dict.values():
        print('All slots are taken. Please cancel a slot if you\'d like to change one.')

    else:
        good_slot = False

        part_name = input('Participant Name: ')

        while not good_slot:
            part_slot = input('Desired Participant Slot #[1-%i]: ' % userNum)
            if part_slot.isdecimal():
                part_slot = int(part_slot)

                if part_slot in participant_dict.keys():

                    if participant_dict[part_slot] is None:
                        participant_dict[part_slot] = part_name
                        good_slot = True
                        saveFlag = False
                        return saveFlag
                    else:
                        print('That slot is already taken. Try another.')

                else:
                    print('Slot not in registry.')

            else:
                print('That is not a number. Try again.')


# We also need a cancel sign up function which would free up a slot.

# In[46]:


def cancel_sign_up(userNum):
    # request user name and slot - if both don't line up or exist, discard and try again
    good_input = False
    null_counter = 0
    for i in range(1, userNum+1):
        if participant_dict[i] == None:
            null_counter = null_counter + 1
    
    if null_counter == len(participant_dict.items()):
        # all empty - nothing to remove!
        print('Sorry, there are no participants. Add participants before trying to remove them.')
    
    else:
        while not good_input:
            part_slot = input('Enter participant slot #[1-%i]: ' % userNum)
            if part_slot.isdecimal():
                part_slot = int(part_slot)

                if part_slot < 1 or part_slot > userNum:
                    print('Number out of range. Please try again.')
                else:
                    part_name = input('Enter participant name: ')

                    if participant_dict[part_slot] == part_name:
                        participant_dict[part_slot] = None
                        print('Participant successfully removed.')
                        good_input = True
                        saveFlag = False
                        return saveFlag
                    else:
                        print('There is no participant with that name in that slot. Try again.')

            else:
                print('That is not a number. Please try again.')


# We need a function to allow us to view participants:

# In[47]:


def view_part(userNum):
    good_input = False
    
    if userNum < 5:
        # do not accept user input, just print what we've got
        for i in range(1, userNum+1):
            print(f'{i}: {participant_dict[i]}')
            
    else:
        # we have more than 5, print more
        
        while not good_input:
            view_input = input(f'Starting Slot #[1-{userNum}]: ')
            
            if view_input.isdecimal():
                view_input = int(view_input)
                if view_input < 0 or view_input > userNum:
                    print('Number out of range. Try again.')
                else:
                    # main meat of this process
                    lower_bound = view_input - 5
                    upper_bound = view_input + 5
                    print('Participant Slot: Participant Name')
                    
                    for x in range(lower_bound, view_input):
                        if x in participant_dict.keys():
                            print(f'{x}: {participant_dict[x]}')
                    for y in range(view_input, upper_bound+1):
                        if y in participant_dict.keys():
                            print(f'{y}: {participant_dict[y]}')
                    good_input = True
            else:
                print('That is not a number. Try again.')


# A way to save the changes is part of the exercise as well, so I've made a function for it below:

# In[48]:


def save_changes(userNum):

    file_front = input('Enter filename to save as: ')
    filename = file_front + '.csv'
    
    f = open(filename,'w')
    for i in range(1, userNum+1):
        f.write(f'{i}, {participant_dict[i]}\n')
        
    saveFlag = True
    return saveFlag


# Finally, our exit function, which will return a flag to tell the main program to stop looping:

# In[49]:


def user_exit(saveFlag):
    good_input = False
    exitFlag = False
    
    if saveFlag:
        exitFlag = True
    else:
        while not good_input:
            print('There are unsaved changes.')
            double_check = input('Are you sure you want to exit? [y/n]: ')
            if double_check == 'y':
                exitFlag = True
                good_input = True
            elif double_check == 'n':
                good_input = True
                exitFlag = False
            else:
                print('I couldn\'t understand that, please input a Y or N.')
                
    return exitFlag


# Now we can construct the main loop:

# In[51]:


exit_flag = False
save_flag = True
while not exit_flag:
    userOption = main_menu()
    
    if userOption == 1:
        save_flag = part_sign_up(userNum)
    elif userOption == 2:
        save_flag = cancel_sign_up(userNum)
    elif userOption == 3:
        view_part(userNum)
    elif userOption == 4:
        save_flag = save_changes(userNum)
    elif userOption == 5:
        exit_flag = user_exit(save_flag)
        


# In[ ]:




