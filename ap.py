import json
from urllib import request

# Server details will change between lab, home, and competition, so saving them somehwere easy to edit
server_ip = "192.168.56.1"
#server_ip = "vpfs.lan"
server = f"http://{server_ip}:5000"
authKey = "45" # For the lab, your auth key is your team number, at competition this will be a secret key
team = 45

def get_fare():
    # Make request to fares endpoint
    res = request.urlopen(server + "/fares")
    # Verify that we got HTTP OK
    if res.status == 200:
        # Decode JSON data
        fares = json.loads(res.read())
        # Loop over the available fares
        for fare in fares:
            # If the fare is claimed, skip it
            if not fare['claimed']:
                # Get the ID of the fare
                toClaim = fare['id']
                
                # Make request to claim endpoint
                res = request.urlopen(server + "/fares/claim/" + str(toClaim) + "?auth=" + authKey)
                # Verify that we got HTTP OK
                if res.status == 200:
                    # Decode JSON data
                    data = json.loads(res.read())
                    if data['success']:
                        # If we have a fare, exit the loop
                        print("Claimed fare id", toClaim)
                        break
                    else:
                        # If the claim failed, report it and let the loop continue to the next
                        print("Failed to claim fare", toClaim, "reason:", data['message'])
                else:
                    # Report HTTP request error
                    print("Got status", str(res.status), "claiming fare")
    else:
        # Report HTTP request error
        print("Got status", str(res.status), "requesting fares")


    # Check the status of our fare
    res = request.urlopen(server + "/fares/current/" + str(team))
    # Verify that we got HTTP OK
    if (res.status == 200):
        # Decode JSON data
        data = json.loads(res.read())
        # Report fare status
        if fare is not None:
            print("Have fare", data['fare'])
            return ("Claim fare",data['fare'])
        else:
            print("No fare claimed", data['message'])
            return ("no fare",data['message'])
    else:
        # Report HTTP request error
        print("Got status", str(res.status), "checking fare")
        return ("http err",res.status)


def get_locations():
    cur_fares = request.urlopen(server + "/fares/current/" + str(team))
    tmp = cur_fares.read().decode('utf-8')
    fares = json.loads(tmp)
    start_loc_x = int(fares["fare"]["src"]["x"])
    start_loc_y = int(fares["fare"]["src"]["y"])

    end_loc_x = int(fares["fare"]["dest"]["x"])
    end_loc_y = int(fares["fare"]["dest"]["y"])

    ret_val = [start_loc_x, start_loc_y, end_loc_x, end_loc_y]

    return ret_val

def get_current_loc():
    loc = request.urlopen(server + "/WhereAmI/" + str(team))
    tmp = loc.read()
    locs = json.loads(tmp)
    location = [int(locs["position"]["x"]), int(locs["position"]["y"])]
    return location
