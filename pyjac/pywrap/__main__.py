"""Main module for pywrap module.
"""
from argparse import ArgumentParser

from pyjac import utils
from pyjac.pywrap.pywrap_gen import pywrap
from pyjac.core.enum_types import KernelType

if __name__ == '__main__':
    parser = ArgumentParser(
        description='Generates a python wrapper for pyJac via Cython')
    parser.add_argument('-l', '--lang',
                        type=str,
                        choices=utils.langs,
                        required=True,
                        help='Programming language for output '
                             'source files'
                        )
    parser.add_argument('-so', '--source_dir',
                        type=str,
                        required=True,
                        help='The folder that contains the generated pyJac '
                             'files.')
    parser.add_argument('-out', '--out_dir',
                        type=str,
                        required=False,
                        default=None,
                        help='The folder to place the generated library in')
    parser.add_argument('-kt', '--kernel_type',
                        required=False,
                        type=utils.EnumType(KernelType),
                        default='jacobian',
                        help='The type of library to build: {type}'.format(
                            type=str(utils.EnumType(KernelType))))

    args = parser.parse_args()
    pywrap(args.lang, args.source_dir, args.out_dir,
           ktype=args.kernel_type)
