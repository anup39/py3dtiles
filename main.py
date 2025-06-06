import argparse
import os
import time
import uuid
from pathlib import Path
from Options import Options, Stage
from Utils import Utils
from Stages.DecimationStage import DecimationStage
from Stages.SplittingStage import SplitStage
from Stages.TilingStage import TilingStage
import asyncio


async def run_pipeline(opts: Options):
    print("\n *** OBJ to Tiles ***\n")
    
    if not check_options(opts):
        return
        
    # Create output directory
    output_path = Path(opts.output).absolute()
    output_path.mkdir(parents=True, exist_ok=True)
    
    try:
        # Decimation stage
        print(f" => Decimation stage with {opts.lods} LODs")
        decimation_result = await DecimationStage.decimate(
            str(Path(opts.input).absolute()),
            str(output_path),
            opts.lods
        )
        print(" ?> Decimation stage completed")
        print(f" -> Decimated files: {decimation_result.dest_files}")
        print(f" -> Bounds: {decimation_result.bounds}")
        
        if opts.stop_at == Stage.DECIMATION:
            return
        
        # Splitting stage
        out_split = os.path.join(output_path,'split')
        print(f" => Splitting stage with {opts.divisions} divisions")
        split_result = await SplitStage.split_multiple(
            decimation_result.dest_files,
            str(out_split),
            opts.divisions,
            opts.z_split,
            decimation_result.bounds

        )
        print(" ?> Splitting stage completed")
        
        if opts.stop_at == Stage.SPLITTING:
            return
        
        #     # Tiling stage
        # print(" => Tiling stage")
        # tiling_result = await TilingStage.create_tiles(
        #     split_result.dest_files,
        #     split_result.bounds,
        #     str(output_path),
        #     opts.base_error,
        #     opts.latitude,
        #     opts.longitude,
        #     opts.altitude
        # )
        # print(" ?> Tiling stage completed")
        # print(f" -> Tileset created at: {tiling_result.tileset_path}")
            
        # Future stages will go here...
        
    except Exception as e:
        print(f" !> Error: {str(e)}")

def check_options(opts: Options) -> bool:
    if not opts.input or not opts.input.strip():
        print(" !> Input file is required")
        return False
        
    if not os.path.exists(opts.input):
        print(" !> Input file does not exist")
        return False
        
    if not opts.output or not opts.output.strip():
        print(" !> Output folder is required")
        return False
        
    if opts.lods < 1:
        print(" !> LODs must be at least 1")
        return False
        
    if opts.divisions < 0:
        print(" !> Divisions must be non-negative")
        return False
        
    return True

def create_temp_folder(folder_name: str, base_folder: str) -> str:
    temp_folder = os.path.join(base_folder, folder_name)
    os.makedirs(temp_folder, exist_ok=True)
    return temp_folder

def main():
    parser = argparse.ArgumentParser(description='OBJ to Tiles converter')
    parser.add_argument('input', help='Input OBJ file')
    parser.add_argument('output', help='Output folder')
    # parser.add_argument('--stage', choices=[s.value for s in Stage], 
    #                    default=Stage.TILING.value, help='Stage to stop at')
    # Add other arguments similar to C# Options class
    parser.add_argument('--divisions', type=int, default=2, help='Number of divisions for splitting')
    parser.add_argument('--z_split', action='store_true', help='Enable Z-splitting')
    parser.add_argument('--lods', type=int, default=3, help='Number of LODs for decimation')
    parser.add_argument('--keep_original_textures', action='store_true', help='Keep original textures')
    parser.add_argument('--latitude', type=float, help='Latitude for georeferencing')
    parser.add_argument('--longitude', type=float, help='Longitude for georeferencing')
    parser.add_argument('--altitude', type=float, default=0, help='Altitude for georeferencing')
    parser.add_argument('--scale', type=float, default=1.0, help='Scale factor for the model')
    
    args = parser.parse_args()
    opts = Options(**vars(args))

    asyncio.run(run_pipeline(opts))
    
    print("\n *** OBJ to Tiles ***\n")
    
    if not check_options(opts):
        return
        
    opts.output = os.path.abspath(opts.output)
    opts.input = os.path.abspath(opts.input)
    
    os.makedirs(opts.output, exist_ok=True)
    
    pipeline_id = str(uuid.uuid4())
    start_time = time.time()
    
    
if __name__ == "__main__":
    main()