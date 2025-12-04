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
        pass

    def fundraising_campaigns(self, max_money: float):
        pass

    def get_auction_report(self):
        pass


    def _search_by_collector_name(self, collector_name):
        return next((c for c in self.collectors if c.name == collector_name), None)


    def _search_by_artifact_name(self, artifact_name):
        return next((a for a in self.artifacts if a.name == artifact_name), None)

