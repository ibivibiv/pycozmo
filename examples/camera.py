#!/usr/bin/env python

import time

import pycozmo


def on_camera_image(cli, image):
    del cli
    image.save("camera.png", "PNG")


def pycozmo_program(cli):

    angle = (pycozmo.robot.MAX_HEAD_ANGLE_RAD - pycozmo.robot.MIN_HEAD_ANGLE_RAD) / 2
    pkt = pycozmo.protocol_encoder.SetHeadAngle(angle_rad=angle)
    cli.send(pkt)

    pkt = pycozmo.protocol_encoder.EnableCamera(enable=True)
    cli.send(pkt)

    # Wait for image to stabilize.
    time.sleep(1.5)

    cli.add_handler(pycozmo.client.EvtNewRawCameraImage, on_camera_image, one_shot=True)

    # Wait for image to be captured.
    time.sleep(1)


pycozmo.run_program(pycozmo_program)