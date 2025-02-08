requirement
* need to install python and pytest
  - see details on requirements.txt

How to execute this utility from command line
* python3 geoloc-util.py --locations "Bellevue, WA" "98006"
   - output will be followings:
    check with placement name=  Bellevue WA
    Bellevue, Washington US :
    latitude=47.6144219, longitude=-122.192337, local_name=벨뷰
    check with zip code= 98006
    Bellevue, US 98006 :
    latitude=47.5614, longitude=-122.1552

How to run test for this CLI utility
* test (full integration code. assume we are using CLI from test codes)
   - pytest test_geoloc.py in tests folder
   - pytest tests/ in root folder


