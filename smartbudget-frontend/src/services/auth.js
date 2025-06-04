import axios from 'axios';

export const login = async (email, password) => {
  try {
    const response = await axios.post('http://localhost:8000/api/token/', {
      email: email,
      password: password
    });

    // Save the access and refresh token
    localStorage.setItem('access_token', response.data.access);
    localStorage.setItem('refresh_token', response.data.refresh);

    // Set default authorization header for future requests
    axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.access}`;

    return response;
  } catch (error) {
    console.error('Login failed:', error.response?.data || error.message);
    throw error;
  }
};
