
class TestData:
    pairwise_data = [
        (40, "large", False, "high", 700.0),
        (40, "small", False, "other_value", 400.0),
        (20, "small", True, "other_value", 600.0),
        (20, "large", False, "very high", 640.0),
        (20, "small", True, "high", 840.0),
        (20, "large", False, "increased", 480.0),
        (5, "large", True, "increased", 720.0),
        (5, "small", False, "other_value", 400.0),
        (5, "large", True, "very high", 960.0),
        (5,	"small", False, "high", 400.0),
        (1, "small", True, "high", 630.0),
        (1, "large", False, "increased", 400.0),
        (1, "small", True, "other_value", 450.0),
        (1, "large", False, "very high", 400.0)
    ]

    negative_data = [
        (40, "large", True, "very high"),
        (-10, "small", False, "other_value"),
        (0, "large", False, "very_high"),
        (None, "small", True, "increased"),
        (1, None, True, "very high"),
        (20, "large", None, "other_value"),
        (40, "small", True, None),
        (5, "маленький", False, "increased"),
    ]

    distance_boundary_values = [
        (31, "large", False, "high", 700.0),
        (30, "small", False, "other_value", 400.0),
        (29, "small", True, "other_value", 600.0),
        (11, "large", False, "very high", 640.0),
        (10, "small", True, "high", 700.0),
        (9, "large", False, "increased", 400.0),
        (3, "large", True, "increased", 720.0),
        (2, "small", False, "other_value", 400.0),
        (1, "large", True, "very high", 880.0)
    ]
