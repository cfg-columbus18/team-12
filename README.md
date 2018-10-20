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
    bool exists = false;
    for (int i = 0; i < mentor_data.size(); ++i) {
        
        for (int j = 0; j < requested_specialty.size(); ++j) {
            string requested = requested_specialty[j];
            
            
```
