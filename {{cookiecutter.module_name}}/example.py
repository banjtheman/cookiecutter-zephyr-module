import logging
import controller


def main():

    logging.info("Running example")
    formated_input = controller.format_input("hello")
    proccessed_data = controller.procces_data(formated_input)
    formatted_output = controller.format_output(proccessed_data)
    logging.info("Done and done")

if __name__ == "__main__":
    loglevel = logging.INFO
    logging.basicConfig(
        format="%(asctime)s |%(levelname)s: %(message)s", level=loglevel
    )
    main()