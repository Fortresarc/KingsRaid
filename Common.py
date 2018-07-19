import nox

def confirm(properties = None, start_condition = None, notes = []):

    if properties is None:
        properties = {}

    print()

    if len(properties) > 0:
        print('Properties:')
        for (k,v) in properties.items():
            print('  {0}: {1}'.format(k, v))
        if start_condition is not None:
            print('  Start Condition: {0}'.format(start_condition))

        for n in notes:
            print('Note: {0}'.format(n))

    print('Press Enter to confirm or Ctrl+C to cancel. ', end = '')
    nox.do_input()

    print('************************************** WARNING *************************************************')
    print('* Please watch the macro for the first few cycles to make sure everything is working as        *\n'
          '* intended.  If you are selling or grinding gear, make sure your Sell All and Grind All screen *\n'
          '* is pre-configured with the appropriate values.  For extra security, make sure all valuable   *\n'
          '* items are locked.                                                                            *\n'
          '************************************************************************************************')

    nox.wait(500)
