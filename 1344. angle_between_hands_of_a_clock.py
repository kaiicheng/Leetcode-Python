class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # minute
        # 30 min => 180 degree
        # 1 min => 6 degree

        # hour
        # 60 min => 30 degree
        # 1 min => 0.5 degree

        if hour == 12:
            hour = 0

        h_degree = hour * 30 + minutes * 0.5

        m_degree = minutes * 6

        # print("h_degree, m_degree: ", h_degree, m_degree)

        if h_degree > m_degree:
            return min(h_degree - m_degree, 360 - (h_degree - m_degree))
        elif h_degree < m_degree:
            return min(m_degree - h_degree, 360 - (m_degree - h_degree))
        elif h_degree == m_degree:
            return 0

def main(hour, minutes):
    result = Solution()
    print(result.angleClock(hour, minutes))

if __name__== "__main__" :
    hour = 12
    minutes = 30
    main(hour, minutes)
