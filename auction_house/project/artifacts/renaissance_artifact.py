from project.artifacts.base_artifact import BaseArtifact


class RenaissanceArtifact(BaseArtifact):

    @property
    def type(self):
        return "Renaissance Artifact"