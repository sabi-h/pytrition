.PHONY: data
data:
	curl https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_foundation_food_csv_2023-04-20.zip --output ./pytrition/data.zip

.PHONY: clean
clean:
	rm -rf pytrition/data.zip