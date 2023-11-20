import random
import code_folder.main_page.backend_information.treasure.random_magic_items as rmi


class Mission:
    def __init__(self, name, description, objectives, rewards):
        self.name = name
        self.description = description
        self.objectives = objectives
        self.rewards = rewards

class RandomMissionMaker:
    def __init__(self):
        self.mission_types = [
            "Rescue Mission",
            "Exploration Mission",
            "Bounty Hunt",
            "Artifact Retrieval",
            "Assassination Mission",
            "Diplomatic Mission",
            "Mystery Investigation",
            "Heist",
            "Guard or Escort Mission",
            "Rivalry or Tournament",
            "Cursed Item",
            "Invasion Defense",
            "Epic Quest",
            "Political Intrigue",
            "Monster Hunt",
            "Elemental Disturbance",
            "Underdark Exploration",
            "Time Travel or Dimensional Rift"
        ]

    def generate_random_mission(self):
        mission_type = random.choice(self.mission_types)
        name = f"{mission_type} - {random.randint(1, 100)}"
        description = f"This mission involves a {mission_type.lower()}."
        objectives = self.generate_random_objectives(mission_type)
        rewards = self.generate_random_rewards()

        return Mission(name, description, objectives, rewards)

    def generate_random_objectives(self, mission_type):
        if mission_type in ["Rescue Mission", "Bounty Hunt", "Assassination Mission"]:
            return ["Rescue the target", "Capture or defeat the target"]
        elif mission_type in ["Exploration Mission", "Underdark Exploration"]:
            return ["Explore the unknown territory", "Map the caves or dungeons"]
        elif mission_type == "Artifact Retrieval":
            return ["Locate the artifact", "Retrieve the artifact"]
        elif mission_type == "Diplomatic Mission":
            return ["Negotiate peace", "Deliver an important message"]
        elif mission_type == "Mystery Investigation":
            return ["Solve the mysterious deaths", "Investigate the haunted location"]
        elif mission_type == "Heist":
            return ["Plan and execute the heist", "Steal the valuable object"]
        elif mission_type == "Guard or Escort Mission":
            return ["Guard the caravan", "Escort the VIP"]
        elif mission_type == "Rivalry or Tournament":
            return ["Compete in the tournament", "Settle the rivalry through challenges"]
        elif mission_type == "Cursed Item":
            return ["Remove the curse from an item or character", "Investigate the origin of the curse"]
        elif mission_type == "Invasion Defense":
            return ["Defend the town or city", "Repel the attack on the sacred site"]
        elif mission_type == "Epic Quest":
            return ["Embark on a long and perilous journey", "Collect a series of items"]
        elif mission_type == "Political Intrigue":
            return ["Navigate the complex politics", "Uncover and thwart a political conspiracy"]
        elif mission_type == "Monster Hunt":
            return ["Hunt down the dangerous monster", "Investigate mysterious animal attacks"]
        elif mission_type == "Elemental Disturbance":
            return ["Investigate disturbances in the natural elements", "Restore balance to the region"]
        elif mission_type == "Time Travel or Dimensional Rift":
            return ["Travel through time to fix a past mistake", "Deal with the consequences of a dimensional rift"]

        # Default case: return an empty list if the mission type is not recognized
        return []

    def generate_random_rewards(self):
        num_rewards = random.randint(1, 3)
        rewards = []

        for _ in range(num_rewards):
            reward_type = random.choice(["Coin", "Magic Item", "Experience Points"])
            
            if reward_type == "Coin":
                amount = random.randint(10, 100)  # Adjust the range as needed
                rewards.append(f"{amount} gold coins")
            elif reward_type == "Magic Item":
                table_selector = random.randint(1, 9) 
                magic_item = ""
                if table_selector == 1:
                    magic_item = rmi.magic_item_table_a()
                elif table_selector == 2:
                    magic_item = rmi.magic_item_table_b()
                elif table_selector == 3:
                    magic_item = rmi.magic_item_table_c()
                elif table_selector == 4:
                    magic_item = rmi.magic_item_table_d()
                elif table_selector == 5:
                    magic_item = rmi.magic_item_table_e()
                elif table_selector == 6:
                    magic_item = rmi.magic_item_table_f()
                elif table_selector == 7:
                    magic_item = rmi.magic_item_table_g()
                elif table_selector == 8:
                    magic_item = rmi.magic_item_table_h()
                elif table_selector == 9:
                    magic_item = rmi.magic_item_table_i()
                if magic_item is not None:
                    rewards.append(f"Magic item: {magic_item}")
            elif reward_type == "Experience Points":
                xp_amount = random.randint(100, 500)  # Adjust the range as needed
                rewards.append(f"{xp_amount} experience points")

        return rewards

def main():
    mission_maker = RandomMissionMaker()

    for _ in range(5):  # Generate 5 random missions for demonstration
        random_mission = mission_maker.generate_random_mission()
        print(f"\nMission: {random_mission.name}")
        print(f"Description: {random_mission.description}")
        print(f"Objectives: {', '.join(random_mission.objectives) if random_mission.objectives else 'None'}")
        print(f"Rewards: {', '.join(random_mission.rewards)}\n")

if __name__ == "__main__":
    main()