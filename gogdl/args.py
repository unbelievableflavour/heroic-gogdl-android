"""
Android-compatible argument parser for GOGDL
"""

import argparse
from gogdl import constants

def init_parser():
    """Initialize argument parser with Android-compatible defaults"""
    
    parser = argparse.ArgumentParser(
        description='Android-compatible GOG downloader',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        '--auth-config-path',
        type=str,
        default=f"{constants.ANDROID_DATA_DIR}/gog_auth.json",
        help='Path to authentication config file'
    )
    
    parser.add_argument(
        '--display-version',
        action='store_true',
        help='Display version information'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Auth command
    auth_parser = subparsers.add_parser('auth', help='Authenticate with GOG')
    auth_parser.add_argument('--code', type=str, required=True, help='Authorization code from GOG')
    
    # Download command
    download_parser = subparsers.add_parser('download', help='Download a game')
    download_parser.add_argument('id', type=str, help='Game ID to download')
    download_parser.add_argument('--path', type=str, default=constants.ANDROID_GAMES_DIR, help='Download path')
    download_parser.add_argument('--platform', type=str, default='windows', choices=['windows', 'linux'], help='Platform')
    download_parser.add_argument('--branch', type=str, help='Game branch to download')
    download_parser.add_argument('--skip-dlcs', action='store_true', help='Skip DLC downloads')
    download_parser.add_argument('--workers-count', type=int, default=2, help='Number of worker threads')
    download_parser.add_argument('--file-pattern', type=str, help='File pattern to match')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Get game information')
    info_parser.add_argument('id', type=str, help='Game ID')
    info_parser.add_argument('--platform', type=str, default='windows', choices=['windows', 'linux'], help='Platform')
    
    # Repair command
    repair_parser = subparsers.add_parser('repair', help='Repair/verify game files')
    repair_parser.add_argument('id', type=str, help='Game ID to repair')
    repair_parser.add_argument('--path', type=str, default=constants.ANDROID_GAMES_DIR, help='Game path')
    repair_parser.add_argument('--platform', type=str, default='windows', choices=['windows', 'linux'], help='Platform')
    
    # Save sync command
    save_parser = subparsers.add_parser('save-sync', help='Sync game saves')
    save_parser.add_argument('path', help='Path to sync files')
    save_parser.add_argument('--dirname', help='Cloud save directory name')
    save_parser.add_argument('--timestamp', type=float, default=0.0, help='Last sync timestamp')
    save_parser.add_argument('--prefered-action', choices=['upload', 'download', 'none'], help='Preferred sync action')
    
    return parser.parse_known_args()
