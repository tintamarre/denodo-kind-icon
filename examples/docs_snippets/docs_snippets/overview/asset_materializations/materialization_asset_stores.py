import os

import pandas as pd
from dagster import AssetKey, AssetMaterialization, AssetStore, EventMetadataEntry


# start_marker_0
class PandasCsvAssetStore(AssetStore):
    def get_asset(self, context):
        file_path = os.path.join(["my_base_dir", context.step_key, context.output_name])
        return pd.read_csv(file_path)

    def set_asset(self, context, obj):
        file_path = os.path.join(["my_base_dir", context.step_key, context.output_name])

        obj.to_csv(file_path)

        yield AssetMaterialization(
            asset_key=AssetKey(file_path), description="Persisted result to storage."
        )


# end_marker_0


# start_marker_1
class PandasCsvAssetStoreWithMetadata(AssetStore):
    def get_asset(self, context):
        file_path = os.path.join(["my_base_dir", context.step_key, context.output_name])
        return pd.read_csv(file_path)

    def set_asset(self, context, obj):
        file_path = os.path.join(["my_base_dir", context.step_key, context.output_name])

        obj.to_csv(file_path)

        yield AssetMaterialization(
            asset_key=AssetKey(file_path),
            description="Persisted result to storage.",
            metadata_entries=[
                EventMetadataEntry.int(obj.shape[0], label="number of rows"),
                EventMetadataEntry.float(obj["some_column"].mean(), "some_column mean"),
            ],
        )


# end_marker_1
