import math

space_info = {'cell':[5, 0.12, 25, 2],  # defined rates by ASHRAE 62.1
              'dayroom':[5, 0.06, 30, 1], # cfm/person, cfm/sqft, occ density / 1000sqft, air class
              'guard station':[5, 0.06, 15, 1],
              'booking':[7.5, 0.06, 50, 2],
              'waiting':[7.5, 0.06, 50, 2],
              'daycare_age4':[10, 0.18, 25, 2],
              'daycare_sick':[10, 0.18, 25, 3],
              'classroom5_8':[10, 0.12, 25, 1],
                }



def calc_oa_rates(): # defining function to calc OA rates
  while True:
    space_input = input("What type of space? ").lower() # user input for space type
    space = space_info.get(space_input) # define input as key
    if space is not None: # check to see if input is in space_info dict
      cfm_per_person = space_info[space_input][0]
      cfm_per_sqft = space_info[space_input][1]
      occ_density = space_info[space_input][2]
      air_class = space_info[space_input][3]
      break
      #print(cfm_per_person, cfm_per_sqft, occ_density, air_class)
    else:
      print("Invalid input, please enter allowable space type.")
      pass
  length_input_ft = float(input("Provide length of space in feet. "))
  width_input_ft = float(input("Provide width of space in feet. "))

  sqft = int(length_input_ft*width_input_ft)
  oa_per_person = (sqft/occ_density)*cfm_per_person
  oa_sqft = sqft*cfm_per_sqft
  total_oa = math.ceil(oa_per_person+oa_sqft)
  print('Space Type: ' + space_input.title() + '\n' +
        'Space Square Feet: ' + str(sqft) + '\n')

calc_oa_rates()