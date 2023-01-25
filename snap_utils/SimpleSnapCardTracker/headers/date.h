#pragma once
#include <iostream>
#include <string>

class date
{
	public:
		date(unsigned int day, unsigned int month, unsigned int year);
		date();
		std::string getFormattedDate();

		int getDay() {
			return this->day;
		}
		int getMonth() {
			return this->month;
		}
		int getYear() {
			return this->year;
		}

		void setDate(unsigned int day, unsigned int month, unsigned int year);

	private:
		int day = 0;
		int month = 0;
		int year = 0;
		
		const std::string monthList[12] = 
			{"January", "Feburary", "March", "April", 
			"May", "June", "July", "August", "September", 
			"October", "November", "December"};

};

date::date() {

}

date::date(unsigned int day, unsigned int month, unsigned int year) {
	setDate(day, month, year);
}

void date::setDate(unsigned int day, unsigned int month, unsigned int year)
{
	if (day < 1 || day > 31)
	{
		throw std::invalid_argument("Day is invalid. Must be between 1 and 31.");
	}
	if (month < 1 || month > 12)
	{
		throw std::invalid_argument("Month is invalid. Must be between 1 and 12.");
	}

	this->day = day;
	this->month = month;
	this->year = year;
}

std::string date::getFormattedDate()
{
	std::string final;
	std::string sp = " ";
	std::string ordinalsuffix = "th";

	//cardinal stuff
	if (day == 1 || day == 21 || day == 31) { ordinalsuffix = "st"; }
	else if (day == 2 || day == 22) { ordinalsuffix = "nd"; }
	else if (day == 3 || day == 23) { ordinalsuffix = "rd"; }

	final = monthList[month - 1] + sp + std::to_string(day) + ordinalsuffix + "," + sp + std::to_string(year);
	return final;
}