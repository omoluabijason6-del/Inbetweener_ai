from core.asset import Asset


class AssetAgent:
    """
    Manages project assets.
    """

    def __init__(self):
        self.name = "Asset Agent"
        self.assets = []

    def start(self):
        print("[Asset] Ready.")

    def add_asset(
        self,
        name,
        path,
        asset_type
    ):
        asset = Asset(
            name=name,
            path=path,
            asset_type=asset_type
        )

        self.assets.append(asset)

        print(f"[Asset] Registered '{name}'")

        return asset

    def get_assets(self):
        return self.assets