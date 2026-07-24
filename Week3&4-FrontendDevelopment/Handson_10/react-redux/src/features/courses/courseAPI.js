import axios from "axios";

const API_URL = "https://jsonplaceholder.typicode.com/posts";

export const fetchCoursesAPI = async () => {
  const response = await axios.get(API_URL);
  return response.data.slice(0, 10);
};