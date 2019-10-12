#! /usr/bin/env python

'''
Render region
'''

import sys
import argparse
import bpy # pylint: disable=import-error

def main():
    '''
    Run
    '''

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('min_x', type=float, help="min x")
    parser.add_argument('min_y', type=float, help="min y")
    parser.add_argument('max_x', type=float, help="max x")
    parser.add_argument('max_y', type=float, help="max y")
    parser.add_argument('output', help="output PNG file")

    argv = sys.argv[sys.argv.index('--') + 1:]
    args = parser.parse_args(argv)

    # Set region
    bpy.context.scene.render.border_min_x = args.min_x
    bpy.context.scene.render.border_min_y = args.min_y
    bpy.context.scene.render.border_max_x = args.max_x
    bpy.context.scene.render.border_max_y = args.max_y
    bpy.context.scene.render.use_border = True

    # Render
    filepath = '%s-%s-%s-%s-%s' % tuple(argv)
    bpy.data.scenes['Scene'].render.filepath = filepath
    bpy.ops.render.render(write_still=True)


if __name__ == '__main__':
    sys.exit(main())
