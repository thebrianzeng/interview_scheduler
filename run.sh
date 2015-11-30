#!/bin/bash
sudo docker rm interview_scheduler_instance
sudo docker run --name interview_scheduler_instance --net=host -p 6003:6003 -i -t interview_scheduler_img
