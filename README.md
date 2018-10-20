# team-12
# The Refugee Hub Mentor/Mentee Matcher
*Web Application to smartly match mentors and mentees by user selected preferences
* Django Framework
* Easy extensions ready for future implementation
  1. App forum/chatting
  2. Provide more support for extra matching criteria
  3. Multilingual support
  4. Automatic Verification of Mentors
## Mentor/Mentee Matching Algorithm
* Implemented with input from Mentee's profile and custom selected input from mentee side to display smart and user friendly matching
```
Input:
      Mentee information
      Set of all Mentors
      Preferences on a scale of 0 - 10
        - Location
        - Language
        - Refugee Nationality
      Requested Specialty of Mentee (ex. General, Housing, Finance, Friends)
      
Output:
      Set of Mentees ranked from greatest to least in match     
```
## Algorithm Implementation (C++ Code)
```c++
vector<Mentor> best_search(int language_pref, int location_pref, int refugee_pref, vector<string> requested_specialty, vector<Mentor> &mentor_data, Mentee &mentee) {
    vector<int> curr_total(mentor_data.size(), 0);
    // check that required specialty exists
    for (int i = 0; i < mentor_data.size(); ++i) {
        bool exists = false;
        for (int j = 0; j < requested_specialty.size(); ++j) {
            string requested = requested_specialty[j];
            for (int k = 0; k < mentor_data[i].specialty.size(); ++k) {
                if (mentor_data[i].specialty[k] == requested) {
                    exists = true;
                }
            }
        }
        if (!exists) {
            curr_total[i] -= 250;
        }
     }
     
     for (int i = 0; i < mentor_data.size(); ++i) {
        if (mentor_data[i].language == mentee.language) += (language_pref);
        if (mentor_data[i].country == mentee.city) += (location_pref * 0.25);
        if (mentor_data[i].state == mentee.state) += (location_pref * 0.5);
        if (mentor_data[i].city == mentee.city) += (location_pref);
        if (mentor_data[i].refugee_origin == mentee.refugee_origin) += refugee_pref;
     }
     
     // gets 8 best searches
     vector<Mentor> best_search;
     for (int i = 0; i < 8; ++i) {
        int max = curr_total[0];
        int max_idx = 0;
        for (int j = 1; j < mentor_data.size(); ++j) {
            if (curr_total[j] > max) {
              max = curr_total[j];
              max_idx = j;
            }
        }
        best_search.push_back(mentor_data[idx])
        curr_total.erase(curr_total.begin() + idx);
     }
     
     return best_search;
 }         
```
## Alternate Mentor/Mentee Matching Algorithm
* A second mentor/mentee matching algorithm has been implemented in the Matching-Algorithm branch. This algorithm treats the matching process as a multi-objective optimization problem. The algorithm does not require the user to indicate the strength of their preferences, eliminating the need for the user to choose ordinal parameters.
* This algorithm is derived from the multi-objective genetic algorithm NSGA-II.
