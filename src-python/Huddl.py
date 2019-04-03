# userA = [{
#     "meetingID": "1234",
#     "start": 9,
#     "end": 10,
# }, { ... }, { ... }]
# 10 - 11
#
# userB = [{
#     "meetingID": "2234",
#     "start": 10,
#     "end": 11,
# }, { ... }, { ... }]
#
# response = [{
#     "start": 11,
#     "end": 12,
# }, {
#      "start": 12,
#      "end": 13,
# }]

# for each user : get the list of availbe times
# find all the intersections of all the user

def schedule_meeting(userA, userB):

    return list(userA and userB)


def evaluate_free_timings(user):

    ranges = [i for i in range(9,17)] #(9,10)
    counter = 0

    for each_meeting in user:
        if (int(each_meeting['end'])- int(each_meeting['start']) == ranges[counter]):
            ranges.pop(counter)
        counter = counter + 1


    return ranges


if __name__ == '__main__':

    userA = [{
        "meetingID": "1234",
        "start": 9,
        "end": 10,
    },{
        "meetingID": "1234",
        "start": 10,
        "end": 11,
    }, {
        "meetingID": "1234",
        "start": 16,
        "end": 17,
    }]


    userB = [{
        "meetingID": "2234",
        "start": 10,
        "end": 11,
    },{"meetingID": "1234",
        "start": 10,
        "end": 11,
    } , {"meetingID": "1234",
        "start": 10,
        "end": 11,
    }]

    print(evaluate_free_timings(userA))
    print (evaluate_free_timings(userB))

    # response = [{
    #     "start": 11,
    #     "end": 12,
    # }, {
    #      "start": 12,
    #      "end": 13,
    # }]
    #
