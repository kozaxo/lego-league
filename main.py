from pybricks.tools import hub_menu

mission = hub_menu("1", "2", "3")

if mission == "1":
    from mission1 import main

    main()

if mission == "2":
    from mission2 import main

    main()

if mission == "3":
    from lift_test import main

    main()
