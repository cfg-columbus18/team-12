
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

struct Refugee {
    string refugee_origin;
    string refugee_language;
    string refugee_ReasonForRelocation;
};

struct Location {
    string city;
    string state;
    string country;
};

struct Mentor {
    string FirstName;
    string LastName;
    string PhoneNum;
    string email;
    string biography;
    vector<string> contact_preference;
    Refugee refugees;
    Location curr_location;
    
    // unique to mentor
    vector<string> specialty;
};

struct Mentee {
    string FirstName;
    string LastName;
    string PhoneNum;
    string email;
    string biography;
    string contact_preference;
    Refugee refugees;
    Location curr_location;
};




void new_user(Mentee &mentee) {
    string fName, lName, phoneNum, email, bio, contact_preference, ref_origin, ref_language, ref_reason;
    string ccity, cstate, ccountry;
    
    cout << "First Name: ";
    cin >> fName;
    mentee.FirstName = fName;
    cout << "Last Name: ";
    cin >> lName;
    mentee.LastName = lName;
    cout << "Phone Number: ";
    cin >> phoneNum;
    mentee.PhoneNum = phoneNum;
    cout << "Email: ";
    cin >> email;
    mentee.email = email;
    cout << "Biography: ";
    cin >> bio;
    mentee.biography = bio;
    cout << "Contact Preferences: ";
    cin >> contact_preference;
    mentee.contact_preference = contact_preference;
    
    Location loc;
    cout << "Current City: ";
    cin >> ccity;
    loc.city =  ccity;
    cout << "Current State: ";
    cin >> cstate;
    loc.state = cstate;
    cout << "Current Country: ";
    cin >> ccountry;
    loc.country = ccountry;
    mentee.curr_location = loc;
    
    Refugee ref;
    cout << "Refugee Origin: ";
    cin >> ref_origin;
    ref.refugee_origin = ref_origin;
    cout << "Refugee Language: ";
    cin >> ref_language;
    ref.refugee_language = ref_language;
    mentee.refugees = ref;
}


void do_search(vector<Mentor> &mentors, Mentee &mentee) {
    // scale of 0 - 10
    int language_pref;
    cout << "On a scale of 0 - 10 what is your Language Preference: ";
    cin >> language_pref;
    int location_pref;
    cout << "On a scale of 0 - 10 what is your Location Preference: ";
    cin >> location_pref;
    int refugee_pref;
    cout << "On a scale of 0 - 10 what is your Refugee Preference: ";
    cin >> refugee_pref;
    cout << endl;
    
    cout << "What type of advice are you looking for?" << endl;
    cout << "ex. General, Banking, Friends, Healthcare" << endl;
    cout << "% ";
    string advice;
    cin >> advice;
    
    
    
}


void populate_database(vector<Mentor> &mentors) {
    // TODO
}



int main(int argc, char *argv[]) {
    vector<Mentor> mentors;
    Mentee mentee;
    
    populate_database(mentors);
    
    
    
    
    cout << "The Refugee Mentor/Mentee Matcher!" << endl << endl;
    cout << "1: To Login" << endl;
    cout << "2: New User" << endl;
    
    int num;
    cout << "% ";
    cin >> num;
    if (num == 1) {
        new_user(mentee);
    }
    else {
        new_user(mentee);
    }
    
    cout << "There are " << mentors.size() << " in the network!" << endl;
    cout << "1: To do a search" << endl;
    cout << "2: To exit" << endl;
    cout << "% ";
    while (cin >> num && num != 2) {
        cout << endl;
        do_search(mentors, mentee);
        cout << "1: To do a search" << endl;
        cout << "2: To exit" << endl;
        cout << "% ";
    }

    return 0;
}
