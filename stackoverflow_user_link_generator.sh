#!/bin/bash

STACKOVERFLOW_USERS_PAGE='https://stackoverflow.com/users'
TOTAL_USERS=11000000
USER_COUNTER=1

for (( $USER_COUNTER; $USER_COUNTER <= $TOTAL_USERS; ++USER_COUNTER ))
do
    echo "$STACKOVERFLOW_USERS_PAGE/$USER_COUNTER" >> stackoverflow_profile_links.txt
done
