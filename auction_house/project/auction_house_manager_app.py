from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:

    VALID_ARTIFACTS = {
        "RenaissanceArtifact": RenaissanceArtifact,
        "ContemporaryArtifact": ContemporaryArtifact
    }

    VALID_COLLECTORS = {
        "Museum": Museum,
        "PrivateCollector": PrivateCollector
    }

    def __init__(self):
        self.artifacts: list[BaseArtifact] = []
        self.collectors: list[BaseCollector] = []


    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):

        try:
            new_artifact = self.VALID_ARTIFACTS[artifact_type](artifact_name, artifact_price, artifact_space)
        except KeyError:
            raise ValueError("Unknown artifact type!")

        has_already_artifact = self._search_by_artifact_name(artifact_name)
        if has_already_artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."


    def register_collector(self, collector_type: str, collector_name: str):
        try:
            new_collector = self.VALID_COLLECTORS[collector_type](collector_name)
        except KeyError:
            raise ValueError("Unknown collector type!")

        has_already_collector = self._search_by_collector_name(collector_name)
        if has_already_collector:
            raise ValueError(f"{collector_name} has been already registered!")

        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."


    def perform_purchase(self, collector_name: str, artifact_name: str):
        curr_collector = self._search_by_collector_name(collector_name)
        if curr_collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        curr_artifact = self._search_by_artifact_name(artifact_name)
        if curr_artifact is None:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not curr_collector.can_purchase(curr_artifact.price, curr_artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(curr_artifact)
        curr_collector.purchased_artifacts.append(curr_artifact)
        curr_collector.available_money -= curr_artifact.price
        curr_collector.available_space -= curr_artifact.space_required
        return f"{collector_name} purchased {artifact_name} for a price of {curr_artifact.price:.2f}."


    def remove_artifact(self, artifact_name: str):
        curr_artifact = self._search_by_artifact_name(artifact_name)
        if curr_artifact is None:
            return "No such artifact."

        self.artifacts.remove(curr_artifact)
        return f"Removed {curr_artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        filtered_collectors = self._extract_collectors_with_less_or_equal_money(max_money)
        count_filtered_collectors = len(filtered_collectors)
        [c.increase_money() for c in filtered_collectors]
        return f"{count_filtered_collectors} collector/s increased their available money."

    def _extract_collectors_with_less_or_equal_money(self, money) -> list[BaseCollector] | None:
        collectors = [ c for c in self.collectors if c.available_money <= money]
        return collectors if collectors else None



    def get_auction_report(self) -> str:

        count_of_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)
        count_of_available_artifacts = len(self.artifacts)

        sorted_collectors = sorted(self.collectors,
                                   key=lambda c: (-len(c.purchased_artifacts), c.name))

        result = [
            "**Auction statistics**",
            f"Total number of sold artifacts: {count_of_sold_artifacts}",
            f"Available artifacts for sale: {count_of_available_artifacts}",
            "***",
        ]

        for collector in sorted_collectors:
            result.append(collector.__str__())

        return '\n'.join(result)


    def _search_by_collector_name(self, collector_name):
        return next((c for c in self.collectors if c.name == collector_name), None)


    def _search_by_artifact_name(self, artifact_name):
        return next((a for a in self.artifacts if a.name == artifact_name), None)

