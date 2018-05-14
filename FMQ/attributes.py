from dotmap import DotMap

attributes_map = {
    "all": [
        "AerialAbility", "CommandOfArea", "Communication", "Eccentricity", "Handling",
        "Kicking", "OneOnOnes", "Reflexes", "RushingOut", "TendencyToPunch",
        "Throwing", "Aggression", "Anticipation", "Bravery", "Composure",
        "Concentration", "Decisions", "Determination", "Flair", "Leadership",
        "OffTheBall", "Positioning", "Teamwork", "Vision", "Workrate", "Corners",
        "Crossing", "Dribbling", "Finishing", "FirstTouch", "Freekicks", "Heading",
        "LongShots", "Longthrows", "Marking", "Passing", "PenaltyTaking", "Tackling",
        "Technique", "Acceleration", "Agility", "Balance", "Jumping",
        "NaturalFitness", "Pace", "Stamina", "Strength",
    ],
    "goalkeeping": [
        "AerialAbility", "CommandOfArea", "Communication", "Eccentricity", "Handling",
        "Kicking", "OneOnOnes", "Reflexes", "RushingOut", "TendencyToPunch",
        "Throwing",
    ],
    "mental": [
        "Aggression", "Anticipation", "Bravery", "Composure", "Concentration",
        "Decisions", "Determination", "Flair", "Leadership", "OffTheBall",
        "Positioning", "Teamwork", "Vision", "Workrate",
    ],
    "technical": [
        "Corners", "Crossing", "Dribbling", "Finishing", "FirstTouch", "Freekicks",
        "Heading", "LongShots", "Longthrows", "Marking", "Passing", "PenaltyTaking",
        "Tackling", "Technique",
    ],
    "physical": [
        "Acceleration", "Agility", "Balance", "Jumping", "NaturalFitness", "Pace",
        "Stamina", "Strength",
    ],
    "footedness": [
        "LeftFoot", "RightFoot",
    ],
    "hidden": [
        "Consistency", "Dirtiness", "ImportantMatches", "InjuryProness",
        "Versatility", "Adaptability", "Ambition", "Loyalty", "Pressure",
        "Professional", "Sportsmanship", "Temperament", "Controversy",
    ]
}

attributes = DotMap(attributes_map)
