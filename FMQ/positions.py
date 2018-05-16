#!/usr/bin/python

from dotmap import DotMap

positions_map = {
    "all": [
        "Goalkeeper", "DefenderCentral", "Sweeper", "DefenderLeft", "WingBackLeft",
        "DefenderRight", "WingBackRight", "DefensiveMidfielder", "MidfielderCentral",
        "MidfielderLeft", "MidfielderRight", "AttackingMidCentral", "AttackingMidLeft",
        "AttackingMidRight", "Striker"
    ],
    "GK": ["Goalkeeper"],
    "CB": ["DefenderCentral", "Sweeper"],
    "LB": ["DefenderLeft", "WingBackLeft"],
    "RB": ["DefenderRight", "WingBackRight"],
    "DM": ["DefensiveMidfielder"],
    "CM": ["MidfielderCentral"],
    "LM": ["MidfielderLeft"],
    "RM": ["MidfielderRight"],
    "AM": ["AttackingMidCentral"],
    "LF": ["AttackingMidLeft"],
    "RF": ["AttackingMidRight"],
    "ST": ["Striker"],
}

positions = DotMap(positions_map)
