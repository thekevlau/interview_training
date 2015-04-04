
#i am a company. i am starting a bunch of AWS server instances. they need names. by team name or their function (ie. accounting, risk, infra etc)
# but a team might have multiple machines. so we'll just number them.
# acct 1, acct 2 etc...

#tracker class.

#.allocate(teamname) returns teamname n

#you can also de-allocate machines.




class Tracker (object):
    main_hash = {}

# in key word for checking belonging
    def allocate (server_name):
        #if not main_hash[server_name]:  # bug here
        if server_name not in main_hash:
            #main_hash[server_name] = list[]  # syntax error
            main_hash[server_name] = instances_list[]
            main_hash[server_name].append(True)
            list_length = 1

        else:
            for index, val in enumerate(main_hash[server_name]):
                if not val:
                    main_hash[server_name][index] = True
                    list_length = index
                    break
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

tracker = Tracker()
tracker.allocate("accounting")
tracker.allocate("accounting")
tracker.allocate("accounting")
tracker.deallocate("accounting", 2)
tracker.allocate("accounting")
tracker.allocate("risk")

# ask if efficiency matters
# can we simplify the problem?
    # or, solve it for a simpler case first (abstract it!)
# write unit test. pass it.
