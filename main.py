import ArgParse
import IOHandle
from sys import stderr


def main() -> None:
    try:
        args = ArgParse.ArgParse()
        args.parseArgs()
        IOHandle.IOHandle(args)
    except ValueError:
        print('No script parameter can be empty!', file=stderr)
    except TypeError:
        print('The output file must be the JSON format (.json)', file=stderr)
    except FileNotFoundError:
        print('The input file could not be found!', file=stderr)
    except Exception:
        print('An unexpected error has occured!', file=stderr)


if __name__ == '__main__':
    main()
