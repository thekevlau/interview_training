
#i am a company. i am starting a bunch of AWS server instances. they need names. by team name or their function (ie. accounting, risk, infra etc)
# but a team might have multiple machines. so we'll just number them.
# acct 1, acct 2 etc...

#tracker class.

#.allocate(teamname) returns teamname n

#you can also de-allocate machines.

from sys import stdin

class Tracker (object):
    main_hash = {}

# in key word for checking belonging
    def allocate (server_name):
        # if the server_name DNE yet,
        #if not main_hash[server_name]:  # bug here
        if str(server_name) not in main_hash:
            #main_hash[server_name] = list[]  # syntax error
            #main_hash[server_name] = instances_list[]
            main_hash[server_name] = instances_list[0]
            main_hash[server_name].append(True)
            list_length = 1

        # if the server_name already exists,
        else:
            # iterate through a given server_name's list of instances
            for index, val in enumerate(main_hash[server_name]):
                # if we find a hole in the list (where a value previously existed)
                if val is False:
                    main_hash[server_name][index] = True
                    list_length = index
                    break
                # if we get to the end
            else:
                main_hash[server_name].append(True)
                list_length = len(main_hash[server_name])
            # something that you might want to do here...
            # test case: above test case

        instance_name = server_name + str(list_length)
        #print instance_name  # not really necessary
        return instance_name

    def deallocate(base_server_name, suffix_number):
        #if not main_hash[base_server_name]:  # same bug as above
        if base_server_name not in main_hash:
            return None

        #else if len(main_hash[base_server_name]) != suffix_number:  # syntax error
        elif len(main_hash[base_server_name]) != suffix_number:
            return None

        else:
            main_hash[base_sever_name][suffix_number] = False



# ask if efficiency matters
# can we simplify the problem?
    # or, solve it for a simpler case first (abstract it!)
# write unit test. pass it.
