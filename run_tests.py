from tests.test_main import (
    test_classify_orders_mixed_cases,
    test_classify_orders_treats_nan_like_blank_cells,
    test_summarize_orders_basic,
)


def main():
    try:
        test_classify_orders_mixed_cases()
        print("test_classify_orders_mixed_cases: OK")
    except AssertionError as e:
        print("test_classify_orders_mixed_cases: FAIL")
        raise

    try:
        test_classify_orders_treats_nan_like_blank_cells()
        print("test_classify_orders_treats_nan_like_blank_cells: OK")
    except AssertionError as e:
        print("test_classify_orders_treats_nan_like_blank_cells: FAIL")
        raise

    try:
        test_summarize_orders_basic()
        print("test_summarize_orders_basic: OK")
    except AssertionError as e:
        print("test_summarize_orders_basic: FAIL")
        raise


if __name__ == '__main__':
    main()
