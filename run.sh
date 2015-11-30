#!/bin/bash
sudo docker kill interview_scheduler_instance
sudo docker rm interview_scheduler_instance
sudo docker run \
    --name interview_scheduler_instance \
    --net=host \
    -p 6003:6003 \
    -v /srv/when2interview/logs:/opt/logs \
    -d \
    -i -t interview_scheduler_img
