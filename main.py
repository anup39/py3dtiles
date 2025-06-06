import argparse
import os
import time
import uuid
from pathlib import Path
from options import Options
import asyncio


async def run_pipeline(opts: Options):
    print("\n *** OBJ to Tiles ***\n")
    
    if not check_options(opts):
        return
        
    output_path = Path(opts.output).absolute()
    output_path.mkdir(parents=True, exist_ok=True)
    
    try:
        # Reduction step
        print(f" => Decimation stage with {opts.lods} LODs")
        print(" ?> Decimation stage completed")
        

        # Splitting stage
        out_split = os.path.join(output_path,'split')
        print(f" => Splitting stage with {opts.divisions} divisions")
        print(" ?> Splitting stage completed")
        
    
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
    parser.add_argument('--divisions', type=int, default=2, help='Number of divisions for splitting')
    parser.add_argument('--lods', type=int, default=3, help='Number of LODs for decimation')
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