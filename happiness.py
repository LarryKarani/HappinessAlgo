class HappinessAlgo(object):

    def life_rules(self):
        print("In life happiness is the difference between what life or\n"
              " our current situation is and what you expect it to be")
        print("=====================================================")
        while True:
            state = input(" are you happy or sad> ")
            state = state.lower()
            if state == "happy":
                print("way to go stay happy!... ")
                break
            elif state == "sad":
                print("sorry pall!.... do you think you can solve your problems?")
                answer = input("please type yes or no> ")
                answer = answer.lower()
                if answer == "yes":
                    print("Listen soldier this what your going to do \n"
                          " write down in a step by step format the solution \n "
                          "to your problems and  in a gif of a second \n"
                          "I REPEAT a gif of second start working on your first ste\n"
                          "immediately I promise you will feel better after this\n"
                          " all the best cadet :)")
                    break
                elif answer == "no":
                    print(" Happiness is the difference between what we expect life to be and what it realy is \n "
                          "At times life can be a pain in the wrong spot drifting as away from our expectations  \n "
                          "in order to remain happy we should be at peace\n"
                          " and accept the circustance that life has brought to as \n"
                          " and from that point we will achieve happiness :) ")
                    break
                else:
                    print("please reply with 'yes' or 'no' ")
            else:
                print("please reply with sad or happy")
larry = HappinessAlgo()
larry.life_rules()
